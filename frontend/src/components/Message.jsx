import React from 'react';

const Message = ({ sender, text }) => {
  return (
    <div className={`message ${sender === 'bot' ? 'bot' : 'user'}`}>
      <strong>{sender === 'bot' ? 'AI' : 'You'}:</strong> {text}
    </div>
  );
};

export default Message;
