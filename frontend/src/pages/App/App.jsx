import React from 'react';
import './App.css';

// Components
import Auth from '../Auth/Auth';
import NavBar from '../../components/NavBar/NavBar';

// Pages

export default function App() {
  return (
    <main>
      <NavBar />
      <Auth />
      <div>App</div>
    </main>
  );
}
