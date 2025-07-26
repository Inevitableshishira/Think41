import React, { createContext, useContext, useState, useEffect } from "react";

const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState(null);

  // ✅ Milestone 8 additions:
  const [sessions, setSessions] = useState([]);
  const [selectedSession, setSelectedSession] = useState(null);

  useEffect(() => {
    // Mock session data
    setSessions([
      { id: 1 },
      { id: 2 },
      { id: 3 }
    ]);
  }, []);

  return (
    <ChatContext.Provider
      value={{
        messages,
        setMessages,
        userInput,
        setUserInput,
        loading,
        setLoading,
        conversationId,
        setConversationId,
        sessions,
        setSessions,
        selectedSession,
        setSelectedSession
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => useContext(ChatContext);
