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
      <h1>Ваш гид по МИСИС</h1>
      <p>Введите пароль, чтобы продолжить</p>
    </div>
  );
};

export default AdminPanel;
