const express = require('express');

const app = express();

const recipes = [
  { id: 1, name: 'Lasanha', price: 40.0, waitTime: 30 },
  { id: 2, name: 'Macarrão a Bolonhesa', price: 35.0, waitTime: 25 },
  { id: 3, name: 'Macarrão com molho branco', price: 35.0, waitTime: 25 },
];

app.get('/receitas/:id', (req, res) => {
  const { id } = req.params;
  const dados = recipes.find((receita) => receita.id === parseInt(id));

  if(!dados) return res.status(404).json({});
  res.status(200).json(dados);
});

app.put('/', (req, res) => res.send('Olá endpoint PUT'));

app.post('/', (req, res) => res.send('Olá endpoint POST'));

app.delete('/', (req, res) => res.send('Olá endpoint DELETE'));

app.listen(3000, () => console.log('Porta 3000 ativa!'));