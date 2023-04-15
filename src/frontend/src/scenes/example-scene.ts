export class ExampleScene extends Phaser.Scene {
  create() {
    this.add.text(10, 10, "Enter your name:", {
      font: "32px Courier",
      color: "#ffffff",
    });

    const textEntry = this.add.text(10, 50, "", {
      font: "32px Courier",
      color: "#ffff00",
    });

    this.input.keyboard.on(
      "keydown",
      (event: { keyCode: number; key: string }) => {
        if (event.keyCode === 8 && textEntry.text.length > 0) {
          textEntry.text = textEntry.text.substr(0, textEntry.text.length - 1);
        } else if (
          event.keyCode === 32 ||
          (event.keyCode >= 48 && event.keyCode < 90)
        ) {
          textEntry.text += event.key;
        } else if (event.keyCode === 13) {
          alert("You entered: " + textEntry.text);
          textEntry.text += "\n";
        }
      }
    );
  }
}
