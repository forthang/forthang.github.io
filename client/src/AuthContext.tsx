import React, { createContext, useContext, useState, useEffect } from 'react';

interface AuthContextType {
  isAuthenticated: boolean;
  setIsAuthenticated: (auth: boolean) => void;
  serverResponse: string | null; 
  setServerResponse: (response: string | null) => void;
  login: (token: string) => void; 
  logout: () => void; 
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    const token = localStorage.getItem('authToken');
    return !!token; 
  });
  const [serverResponse, setServerResponse] = useState<string | null>(null);

  const login = (token: string) => {
    setIsAuthenticated(true);
    localStorage.setItem('authToken', token); 
    console.log('User logged in:', token); 
  };

  const logout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('authToken');
    console.log('User logged out'); 
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated, serverResponse, setServerResponse, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
