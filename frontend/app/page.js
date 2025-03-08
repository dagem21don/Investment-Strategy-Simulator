"use client";

import { useState } from "react";

export default function Home() {
  const [data, setData] = useState([]);

  const fetchStock = async () => {
    const response = await fetch("http://127.0.0.1:8000/stock/AAPL");
    const result = await response.json();
    setData(result);
  };

  return (
    <div className="p-5">
      <h1 className="text-xl font-bold">Investment Strategy Simulator</h1>
      <button onClick={fetchStock} className="p-2 bg-blue-500 text-white rounded">Get AAPL Data</button>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
