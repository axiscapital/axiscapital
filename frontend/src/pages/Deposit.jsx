
import React, { useState } from 'react';
import api from '../api/axios';
export default function Deposit() {
  const [amount, setAmount] = useState('');
  const handleSubmit = async e => {
    e.preventDefault();
    const res = await api.post('/payments/deposit/', {amount_usdt: amount});
    window.location.href = res.data.checkoutUrl;
  };
  return (
    <form onSubmit={handleSubmit}>
      <h2>Deposit USDT via Binance</h2>
      <input type="number" step="0.01" value={amount} onChange={e=>setAmount(e.target.value)} placeholder="Amount USDT"/>
      <button type="submit">Pay with Binance</button>
    </form>
  );
}
