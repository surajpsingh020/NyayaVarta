import React from 'react';

function NotificationList({ notifications }) {
  return (
    <ul>
      {notifications.map(n => (
        <li key={n.id} className={n.is_read ? 'text-gray-500' : 'font-bold'}>
          {n.message}
        </li>
      ))}
    </ul>
  );
}

export default NotificationList;
