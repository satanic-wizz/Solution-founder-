import React, { useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

const SolutionFinderAI = () => {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleQuery = async () => {
    setLoading(true);
    try {
      const res = await axios.post("https://api.siputzx.my.id/api/ai/deepseek", { query: input });
      setResponse(res.data.solution);
    } catch (error) {
      setResponse("Error fetching solution");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-green-400 to-blue-500 p-4 text-white">
      <h1 className="text-4xl font-bold mb-6">Solution Finder AI</h1>
      <motion.input
        whileFocus={{ scale: 1.05 }}
        className="w-full max-w-md p-3 rounded-lg text-black"
        placeholder="Enter your problem..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <motion.button
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
        className="mt-4 px-6 py-3 bg-yellow-500 rounded-lg shadow-lg"
        onClick={handleQuery}
        disabled={loading}
      >
        {loading ? "Thinking..." : "Find Solution"}
      </motion.button>
      <div className="mt-6 bg-white text-black p-4 rounded-lg w-full max-w-md">
        {response && <p>{response}</p>}
      </div>
    </div>
  );
};

export default SolutionFinderAI;
