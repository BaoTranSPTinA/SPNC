const API_BASE = localStorage.getItem("spnc_api") || "http://127.0.0.1:8000/api";

function getToken() {
  return localStorage.getItem("spnc_token") || "";
}

async function apiFetch(path, options = {}) {
  const headers = Object.assign(
    { "Content-Type": "application/json" },
    options.headers || {}
  );
  const token = getToken();
  if (token) headers["Authorization"] = `Bearer ${token}`;
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  if (!res.ok) throw new Error(`API ${res.status}`);
  return res.json();
}

async function login(username, password) {
  const res = await fetch(`${API_BASE}/auth/token/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  if (!res.ok) throw new Error("Đăng nhập thất bại");
  const data = await res.json();
  localStorage.setItem("spnc_token", data.access);
  return data;
}

window.API = { apiFetch, login };


