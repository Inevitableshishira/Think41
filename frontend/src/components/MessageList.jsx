import React from 'react';
import Message from './Message';

const MessageList = ({ messages }) => {
  return (
    <div className="flex flex-col gap-2 p-4 overflow-y-auto h-full">
      {messages.map((msg, index) => (
        <Message key={index} sender={msg.sender} text={msg.message} />
      ))}
    </div>
  );
};

export default MessageList;
