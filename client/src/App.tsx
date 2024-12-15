import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import {Map} from './components/Map';
import Auth from './components/Auth';
import AdminPanel from './components/AdminPanel';
import  {AuthProvider}  from './AuthContext'; 

const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Map />} />
          <Route path="/auth-adm" element={<Auth />} />
          <Route path="/admin" element={<AdminPanel />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;