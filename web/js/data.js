// Minimal demo dataset inferred from ERD
window.DB = {
  algorithms: [
    { algo_id: 1, name: "BFS", description: "Duyệt theo chiều rộng", type: "graph", created_at: "2025-01-01" },
    { algo_id: 2, name: "DFS", description: "Duyệt theo chiều sâu", type: "graph", created_at: "2025-01-02" },
    { algo_id: 3, name: "Dijkstra", description: "Đường đi ngắn nhất", type: "graph", created_at: "2025-01-03" }
  ],
  tutorials: [
    { tutorial_id: 1, algo_id: 1, title: "Giới thiệu BFS", media_url: "", content: "Khái niệm, hàng đợi, từng bước" },
    { tutorial_id: 2, algo_id: 3, title: "Hiểu Dijkstra", media_url: "", content: "Ưu tiên, relax cạnh" }
  ],
  games: [
    { game_id: 1, algo_id: 1, description: "Đi qua mê cung bằng BFS", level: "dễ", max_score: 100 },
    { game_id: 2, algo_id: 3, description: "Tìm đường nhanh nhất", level: "vừa", max_score: 200 }
  ]
};


