import React from 'react';

function ModuleCard({ module }) {
  return (
    <div className="border rounded p-4 m-2 shadow">
      <h3 className="font-bold">{module.title}</h3>
      <p>{module.description}</p>
      <p className="text-sm text-gray-500">Language: {module.language}</p>
    </div>
  );
}

export default ModuleCard;
