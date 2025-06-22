
import React, { useState } from 'react';
import api from '../api/axios';
export default function Login() {
  const [form, setForm] = useState({username:'', password:''});
  const handleChange = e => setForm({...form, [e.target.name]: e.target.value});
  const submit = async e => {
    e.preventDefault();
    await api.post('/auth/login/', form);
    window.location.href='/dashboard';
  };
  return (
    <form onSubmit={submit}>
      <h2>Login</h2>
      <input name="username" placeholder="Username" onChange={handleChange}/>
      <input type="password" name="password" placeholder="Password" onChange={handleChange}/>
      <button type="submit">Login</button>
    </form>
  );
}
