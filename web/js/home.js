document.getElementById("year").textContent = new Date().getFullYear();

const featured = document.getElementById("featured");
const pick = window.DB.algorithms.slice(0, 3);

featured.innerHTML = pick.map(a => `
  <div class="card">
    <div class="badge">${a.type}</div>
    <h4>${a.name}</h4>
    <p>${a.description}</p>
    <a class="btn" href="pages/algorithms.html#${a.algo_id}">Xem chi tiết</a>
  </div>
`).join("");


