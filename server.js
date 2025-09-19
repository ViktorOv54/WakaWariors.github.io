import express from "express";
import fetch from "node-fetch"; // Node 18+ can use native fetch
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 3000;

// Endpoint for AI requests
app.post("/api/chat", async (req, res) => {
  const { question } = req.body;
  const OPENAI_API_KEY = process.env.OPENAI_API_KEY; // Set your key in env

  if (!OPENAI_API_KEY) return res.status(500).json({ error: "OpenAI API key missing" });

  try {
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${OPENAI_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: question }],
        max_tokens: 500,
      }),
    });

    const data = await response.json();
    res.json({ reply: data.choices[0].message.content });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Something went wrong" });
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));