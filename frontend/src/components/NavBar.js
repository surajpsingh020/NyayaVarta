import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="bg-blue-600 p-4 text-white flex justify-between">
      <div className="font-bold">NyayaVarta</div>
      <div>
        <Link to="/" className="mr-4">Home</Link>
        <Link to="/modules" className="mr-4">Modules</Link>
        <Link to="/quiz/1">Quiz</Link>
      </div>
    </nav>
  );
}

export default Navbar;
