export class ExampleScene extends Phaser.Scene {
  async preload() {
    this.load.image("campfire", "assets/campfire.png");
    this.load.image("mage", "assets/mage.png");
    this.load.html("message-form", "assets/text/message-form.html");
  }
  async create() {
    this.add.image(400, 500, "campfire");
    this.add.image(300, 500, "mage");
    this.createSpeechBubble(
      100,
      100,
      600,
      300,
      "With your message, I contemplate about the meaning of life."
    );
    let update = (message: string) => {
      this.createSpeechBubble(100, 100, 600, 300, message);
    };

    const element = this.add.dom(400, 0).createFromCache("message-form");
    element.addListener("click");
    element.on("click", async function (event: any) {
      if (event.target.name === "sendButton") {
        const inputText = this.getChildByName("messageField");

        // Have they entered anything?
        if (inputText.value !== "") {
          const message = inputText.value;

          const response = await fetch("http://127.0.0.1:5000/api/note", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            body: JSON.stringify({
              message: message,
            }),
          });
          if (!response.ok) {
            throw new Error(`Error! status: ${response.status}`);
          }
          const result = (await response.json()) as NoteResponse;
          update(result.message);
        }
      }
    });
    this.tweens.add({
      targets: element,
      y: 50,
      duration: 3000,
      ease: "Power3",
    });
  }

  createSpeechBubble(
    x: integer,
    y: integer,
    width: integer,
    height: integer,
    quote: string
  ) {
    const bubbleWidth = width;
    const bubbleHeight = height;
    const bubblePadding = 10;
    const arrowHeight = bubbleHeight / 4;

    const bubble = this.add.graphics({ x: x, y: y });

    //  Bubble shadow
    bubble.fillStyle(0x222222, 0.5);
    bubble.fillRoundedRect(6, 6, bubbleWidth, bubbleHeight, 16);

    //  Bubble color
    bubble.fillStyle(0xffffff, 1);

    //  Bubble outline line style
    bubble.lineStyle(4, 0x565656, 1);

    //  Bubble shape and outline
    bubble.strokeRoundedRect(0, 0, bubbleWidth, bubbleHeight, 16);
    bubble.fillRoundedRect(0, 0, bubbleWidth, bubbleHeight, 16);

    //  Calculate arrow coordinates
    const point1X = Math.floor(bubbleWidth / 7);
    const point1Y = bubbleHeight;
    const point2X = Math.floor((bubbleWidth / 7) * 2);
    const point2Y = bubbleHeight;
    const point3X = Math.floor(bubbleWidth / 7);
    const point3Y = Math.floor(bubbleHeight + arrowHeight);

    //  Bubble arrow shadow
    bubble.lineStyle(4, 0x222222, 0.5);
    bubble.lineBetween(point2X - 1, point2Y + 6, point3X + 2, point3Y);

    //  Bubble arrow fill
    bubble.fillTriangle(point1X, point1Y, point2X, point2Y, point3X, point3Y);
    bubble.lineStyle(2, 0x565656, 1);
    bubble.lineBetween(point2X, point2Y, point3X, point3Y);
    bubble.lineBetween(point1X, point1Y, point3X, point3Y);

    const content = this.add.text(0, 0, quote, {
      fontFamily: "Arial",
      fontSize: 20,
      color: "#000000",
      align: "center",
      wordWrap: { width: bubbleWidth - bubblePadding * 2 },
    });

    const b = content.getBounds();

    content.setPosition(
      bubble.x + bubbleWidth / 2 - b.width / 2,
      bubble.y + bubbleHeight / 2 - b.height / 2
    );
  }
}

type NoteResponse = {
  message: string;
};
