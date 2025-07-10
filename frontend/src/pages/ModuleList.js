import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ModuleList() {
  const [modules, setModules] = useState([]);

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}content/modules/`)
      .then(res => setModules(res.data));
  }, []);

  return (
    <div>
      <h2 className="text-xl font-bold">Legal Modules</h2>
      <ul>
        {modules.map(mod => (
          <li key={mod.id}>{mod.title} ({mod.language})</li>
        ))}
      </ul>
    </div>
  );
}

export default ModuleList;
