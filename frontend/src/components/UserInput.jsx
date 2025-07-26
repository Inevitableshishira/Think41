import React from "react";
import { useChat } from "../context/ChatContext";

const UserInput = () => {
  const { userInput, setUserInput, setMessages, messages, setLoading } = useChat();

  const handleSend = async () => {
    if (!userInput.trim()) return;

    const newMessage = { sender: "user", message: userInput };
    setMessages([...messages, newMessage]);
    setLoading(true);

    const response = await fetch("http://127.0.0.1:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: 1, message: userInput }),
    });

    const data = await response.json();
    setMessages((prev) => [...prev, { sender: "bot", message: data.reply }]);
    setUserInput("");
    setLoading(false);
  };

  return (
    <div>
      <input
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        placeholder="Type your message"
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default UserInput;
