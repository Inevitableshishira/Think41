import ConversationHistoryPanel from './ConversationHistoryPanel';
import React from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';

const ChatWindow = () => {
  return (
  <div style={{ display: 'flex' }}>
    <ConversationHistoryPanel />
    <div style={{ flex: 1 }}>
      <MessageList />
      <UserInput />
    </div>
  </div>
);

export default ChatWindow;
