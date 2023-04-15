export class ExampleScene extends Phaser.Scene {
  async create() {
    this.add.text(10, 10, "Talk to me:", {
      font: "32px Courier",
      color: "#ffffff",
    });

    const textEntry = this.add.text(10, 50, "", {
      font: "32px Courier",
      color: "#ffff00",
    });

    this.input.keyboard.on(
      "keydown",
      async (event: { keyCode: number; key: string }) => {
        if (event.keyCode === 8 && textEntry.text.length > 0) {
          textEntry.text = textEntry.text.substr(0, textEntry.text.length - 1);
        } else if (
          event.keyCode === 32 ||
          (event.keyCode >= 48 && event.keyCode < 90)
        ) {
          textEntry.text += event.key;
        } else if (event.keyCode === 13) {
          alert("Sending message to server: " + textEntry.text);
          const response = await fetch("http://127.0.0.1:5000/api/note", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            body: JSON.stringify({
              message: textEntry.text,
            }),
          });

          textEntry.text += "\n";
          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
          const result = (await response.json()) as NoteResponse;
          textEntry.text += result.message;
        }
      }
    );
  }
}

type NoteResponse = {
  message: string;
};
