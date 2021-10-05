const pegaNum = require('readline-sync');

console.log("Jogo da adivinhação!!!");

const playGame = () => {
  const numGame = Math.floor(Math.random() * 11);
  const jogada = pegaNum.questionInt("Digite um munero entre 0 e 10: ");
  if (jogada === numGame) {
    console.log("Parabéns, número correto!");
  } else {
    console.log(`Opa, não foi dessa vez. O número era ${numGame}!!!`);
  }
};

const letsPlay = () => {
  playGame();
  let JogaDeNovo = pegaNum.questionInt("Jogar outra vez? 1=Sim / 2=Não ");
  if (JogaDeNovo === 1) {
    letsPlay();
  }
}

letsPlay();