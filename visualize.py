import matplotlib.pyplot as plt

def draw_chessboard(solution):
    """
    Draws an 8x8 chessboard with queens placed according to the solution.
    """
    board_size = 8
    fig, ax = plt.subplots()
    # Draw chessboard
    for row in range(board_size):
        for col in range(board_size):
            color = 'white' if (row + col) % 2 == 0 else 'gray'
            rect = plt.Rectangle((col, board_size - row - 1), 1, 1, facecolor=color)
            ax.add_patch(rect)

    # Place queens
    for col, row in enumerate(solution):
        ax.text(col + 0.5, board_size - row - 0.5, '♛', fontsize=24,
                ha='center', va='center', color='red')

    ax.set_xlim(0, board_size)
    ax.set_ylim(0, board_size)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.title("8-Queens Solution")
    plt.tight_layout()
    plt.savefig("solution.png")  # Save image
    plt.show()
