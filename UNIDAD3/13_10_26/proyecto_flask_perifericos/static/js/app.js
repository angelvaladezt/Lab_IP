"use strict";

const elements = {
  appTitle: document.querySelector("#appTitle"),
  appSubtitle: document.querySelector("#appSubtitle"),
  brandImage: document.querySelector("#brandImage"),
  dataLink: document.querySelector("#dataLink"),
  welcomeText: document.querySelector("#welcomeText"),
  loginPanel: document.querySelector("#loginPanel"),
  loginForm: document.querySelector("#loginForm"),
  loginButton: document.querySelector("#loginButton"),
  loginStatus: document.querySelector("#loginStatus"),
  applicationPanel: document.querySelector("#applicationPanel"),
  sessionText: document.querySelector("#sessionText"),
  mainMenu: document.querySelector("#mainMenu"),
  deviceForm: document.querySelector("#deviceForm"),
  deviceType: document.querySelector("#deviceType"),
  saveButton: document.querySelector("#saveButton"),
  formStatus: document.querySelector("#formStatus"),
  recordList: document.querySelector("#recordList"),
  recordCount: document.querySelector("#recordCount"),
};

let configuration = null;

function showStatus(element, message, type = "") {
  element.textContent = message;
  element.className = "status " + type;
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const data = await response.json();
  if (!response.ok) {
    const error = new Error(data.mensaje || "La solicitud no pudo completarse.");
    error.data = data;
    throw error;
  }
  return data;
}

async function loadConfiguration() {
  try {
    configuration = await requestJson("/api/config");
    elements.appTitle.textContent = configuration.titulo;
    elements.appSubtitle.textContent = configuration.subtitulo;
    elements.welcomeText.textContent = configuration.mensaje_bienvenida;
    elements.loginButton.textContent = configuration.botones.login;
    elements.saveButton.textContent = configuration.botones.guardar;
    elements.dataLink.textContent = configuration.enlace.texto;
    elements.dataLink.href = configuration.enlace.url;
    elements.brandImage.src = configuration.imagen.src;
    elements.brandImage.alt = configuration.imagen.alt;
    fillDeviceTypes(configuration.tipos);
  } catch (error) {
    showStatus(elements.loginStatus, "No fue posible cargar la configuración.", "error");
  }
}

function fillDeviceTypes(types) {
  elements.deviceType.replaceChildren();
  const firstOption = document.createElement("option");
  firstOption.value = "";
  firstOption.textContent = "Selecciona un tipo";
  elements.deviceType.append(firstOption);

  types.forEach((type) => {
    const option = document.createElement("option");
    option.value = type;
    option.textContent = type;
    elements.deviceType.append(option);
  });
}

function buildMenu(items) {
  elements.mainMenu.replaceChildren();
  items.forEach((item, index) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = item.texto;
    button.dataset.view = item.id;
    if (index === 0) button.setAttribute("aria-current", "page");
    elements.mainMenu.append(button);
  });
}

function openView(viewId) {
  document.querySelectorAll(".view").forEach((view) => {
    view.hidden = view.id !== viewId;
  });
  elements.mainMenu.querySelectorAll("button").forEach((button) => {
    if (button.dataset.view === viewId) button.setAttribute("aria-current", "page");
    else button.removeAttribute("aria-current");
  });
}

elements.mainMenu.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-view]");
  if (button) openView(button.dataset.view);
});

elements.loginForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(elements.loginForm);
  const credentials = Object.fromEntries(formData.entries());

  elements.loginButton.disabled = true;
  showStatus(elements.loginStatus, "Comprobando credenciales…");

  try {
    const data = await requestJson("/api/login", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(credentials),
    });
    showStatus(elements.loginStatus, data.mensaje, "success");
    elements.sessionText.textContent = "Sesión: " + data.usuario.nombre;
    buildMenu(data.menu);
    elements.loginPanel.hidden = true;
    elements.applicationPanel.hidden = false;
    openView("inicio");
    await loadRecords();
  } catch (error) {
    showStatus(elements.loginStatus, error.message, "error");
  } finally {
    elements.loginButton.disabled = false;
  }
});

elements.deviceForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  clearFieldErrors();
  const formData = new FormData(elements.deviceForm);
  const payload = Object.fromEntries(formData.entries());

  elements.saveButton.disabled = true;
  showStatus(elements.formStatus, "Guardando…");

  try {
    const data = await requestJson("/api/perifericos", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload),
    });
    showStatus(elements.formStatus, data.mensaje, "success");
    elements.deviceForm.reset();
    await loadRecords();
  } catch (error) {
    showStatus(elements.formStatus, error.message, "error");
    showFieldErrors(error.data?.errores || {});
  } finally {
    elements.saveButton.disabled = false;
  }
});

function clearFieldErrors() {
  document.querySelectorAll(".field-error").forEach((element) => {
    element.textContent = "";
  });
}

function showFieldErrors(errors) {
  document.querySelector("#nameError").textContent = errors.nombre || "";
  document.querySelector("#typeError").textContent = errors.tipo || "";
  document.querySelector("#quantityError").textContent = errors.cantidad || "";
}

async function loadRecords() {
  const data = await requestJson("/api/perifericos");
  elements.recordList.replaceChildren();
  data.registros.forEach((record) => {
    const item = document.createElement("li");
    item.textContent = record.cantidad + " × " + record.tipo + ": " + record.nombre;
    elements.recordList.append(item);
  });
  elements.recordCount.textContent = data.total + (data.total === 1 ? " elemento" : " elementos");
}

loadConfiguration();
