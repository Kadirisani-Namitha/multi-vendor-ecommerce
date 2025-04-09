import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import "../styles/Dashboard.css";

const Dashboard = () => {
  const { user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login"); // Redirect to login page after logout
  };

  if (!user) {
    return <p>Please log in to access the dashboard.</p>; // Redirect if no user logged in
  }

  return (
    <div className="dashboard-container">
      <h1>Welcome, {user?.name}!</h1>
      <p>Role: {user?.role}</p>

      {user?.role === "vendor" ? (
        <div className="vendor-dashboard">
          <h2>Vendor Dashboard</h2>
          <p>Manage your products, orders, and profile here.</p>
        </div>
      ) : user?.role === "customer" ? (
        <div className="customer-dashboard">
          <h2>Customer Dashboard</h2>
          <p>Browse products, track orders, and update your account.</p>
        </div>
      ) : (
        <div>Invalid role.</div>
      )}

      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Dashboard;
