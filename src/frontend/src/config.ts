import { ExampleScene } from "./scenes/example-scene";

export const GameConfig: Phaser.Types.Core.GameConfig = {
  title: "Philosopher in a cave",
  width: 800,
  height: 600,
  type: Phaser.AUTO,
  parent: "game",
  scene: [ExampleScene],
};
