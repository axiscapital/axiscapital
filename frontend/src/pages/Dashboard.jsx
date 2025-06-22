
import React from 'react';
import { Link } from 'react-router-dom';
export default function Dashboard() {
  return (
    <div>
      <h1>AxisCapital Dashboard</h1>
      <Link to="/deposit">Make a Deposit</Link>
    </div>
  );
}
