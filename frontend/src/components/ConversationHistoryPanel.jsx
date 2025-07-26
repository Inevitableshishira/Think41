import React, { useContext } from 'react';
import { ChatContext } from '../context/ChatContext';

const ConversationHistoryPanel = () => {
  const { sessions, setSelectedSession } = useContext(ChatContext);

  const handleClick = (session) => {
    setSelectedSession(session);
  };

  return (
    <div style={{ width: '250px', borderRight: '1px solid #ccc', padding: '1rem' }}>
      <h3>History</h3>
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {sessions.map((session) => (
          <li
            key={session.id}
            onClick={() => handleClick(session)}
            style={{ cursor: 'pointer', padding: '0.5rem 0' }}
          >
            Conversation #{session.id}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ConversationHistoryPanel;
