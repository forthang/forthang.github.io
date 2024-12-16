import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Map } from './components/Map';
import Auth from './components/Auth';
import AdminPanel from './components/AdminPanel';
import { AuthProvider } from './AuthContext'; 

const App: React.FC = () => {
  const [buildingNames, setBuildingNames] = useState<string[]>([]); 

  const handleBuildingSaved = (name: string) => {
    setBuildingNames((prev) => [...prev, name]); 
  };

  const handleBuildingSelect = (name: string) => {
    console.log(`Selected building map for ${name}`);
  };

  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Map buildingNames={buildingNames} onBuildingSelect={handleBuildingSelect} />} />
          <Route path="/auth-adm" element={<Auth />} />
          <Route path="/admin" element={<AdminPanel onBuildingSaved={handleBuildingSaved} />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
