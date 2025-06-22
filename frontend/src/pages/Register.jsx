
import React, { useState } from 'react';
import api from '../api/axios';
export default function Register() {
  const [form, setForm] = useState({username:'', email:'', password:'', password2:''});
  const handleChange = e => setForm({...form, [e.target.name]: e.target.value});
  const submit = async e => {
    e.preventDefault();
    await api.post('/users/register/', form);
    alert('Check your email and then login');
  };
  return (
    <form onSubmit={submit}>
      <h2>Register</h2>
      <input name="username" placeholder="Username" onChange={handleChange}/>
      <input name="email" placeholder="Email" onChange={handleChange}/>
      <input type="password" name="password" placeholder="Password" onChange={handleChange}/>
      <input type="password" name="password2" placeholder="Repeat Password" onChange={handleChange}/>
      <button type="submit">Register</button>
    </form>
  );
}
