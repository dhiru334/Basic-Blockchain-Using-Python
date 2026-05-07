import hashlib
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Block class
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()


# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    # ✅ Added function (prints full details)
    def print_chain(self):
        print("\n===== BLOCKCHAIN DETAILS =====\n")
        for block in self.chain:
            print(f"Block {block.index}")
            print("Timestamp      :", block.timestamp)
            print("Data           :", block.data)
            print("Current Hash   :", block.hash)
            print("Previous Hash  :", block.previous_hash)
            print("-" * 60)

    def visualize(self):
        fig, ax = plt.subplots(figsize=(12, 4))
        fig.patch.set_facecolor('#0f172a')  # dark background

        def draw_block(i):
            ax.clear()
            ax.set_facecolor('#0f172a')

            # Layout
            ax.set_ylim(0, 2)
            ax.set_xlim(-1, len(self.chain) * 2.5)
            ax.axis('off')

            for j in range(i + 1):
                block = self.chain[j]
                x = j * 2.5

                # Colors
                if j == 0:
                    color = "#22c55e"
                else:
                    color = "#3b82f6"

                text = f"""Block {block.index}
{block.data}
Hash: {block.hash[:6]}...
Prev: {block.previous_hash[:6]}..."""

                # Glow layer
                ax.text(x, 1, text,
                        ha='center', va='center',
                        fontsize=9,
                        color='white',
                        bbox=dict(boxstyle="round,pad=0.9",
                                  fc=color, ec=color, alpha=0.3))

                # Main box
                ax.text(x, 1, text,
                        ha='center', va='center',
                        fontsize=9,
                        color='white',
                        bbox=dict(boxstyle="round,pad=0.6",
                                  fc=color, ec="white", lw=1.5))

                # Arrows
                if j > 0:
                    ax.annotate("",
                                xy=(x - 0.8, 1),
                                xytext=(x - 1.8, 1),
                                arrowprops=dict(arrowstyle="->",
                                                color="#38bdf8",
                                                lw=3,
                                                alpha=0.3))
                    ax.annotate("",
                                xy=(x - 0.8, 1),
                                xytext=(x - 1.8, 1),
                                arrowprops=dict(arrowstyle="->",
                                                color="#38bdf8",
                                                lw=1.5))

            ax.set_title("Blockchain Visualization",
                         color='white', fontsize=14)

        ani = animation.FuncAnimation(
            fig,
            draw_block,
            frames=len(self.chain),
            interval=1200,
            repeat=False
        )

        plt.show()


# Run
bc = Blockchain()
bc.add_block("Transaction 1")
bc.add_block("Transaction 2")
bc.add_block("Transaction 3")
bc.add_block("Transaction 4")
# ✅ Print full blockchain details
bc.print_chain()

# ✅ Show visualization
bc.visualize()