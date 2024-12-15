import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const AdminPanel: React.FC = () => {
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    navigate('/auth-adm');
    return null;
  }

  return (
    <div>
      <h1>Админ панель</h1>
      <p>Добро пожаловать в админ панель!</p>
    </div>
  );
};

export default AdminPanel;
