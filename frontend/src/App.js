import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import Dashboard from './components/Dashboard';
import PatientDetails from './components/PatientDetails';
import FileUpload from './components/FileUpload';
import Visualization from './components/Visualization';
import './App.css';  // Make sure this points to the correct CSS file path

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route path="/login" component={LoginForm} />
          <Route path="/register" component={RegisterForm} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/patient/:id" component={PatientDetails} />
          <Route path="/upload" component={FileUpload} />
          <Route path="/visualize/:id" component={Visualization} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
