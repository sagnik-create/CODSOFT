document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const resetButton = document.getElementById('reset');
    const player = 'X';
    const ai = 'O';
    let board = Array(9).fill('');

    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });

    resetButton.addEventListener('click', resetGame);

    function handleCellClick(event) {
        const index = event.target.getAttribute('data-index');
        if (board[index] === '') {
            makeMove(index, player);
            if (!isGameOver(board)) {
                const bestMove = getBestMove(board, ai);
                console.log("AI chose index: ", bestMove);
                makeMove(bestMove, ai);
            }
        }
    }

    function makeMove(index, player) {
        board[index] = player;
        cells[index].textContent = player;
    }

    function resetGame() {
        board = Array(9).fill('');
        cells.forEach(cell => {
            cell.textContent = '';
        });
    }

    function isGameOver(board) {
        const winner = getWinner(board);
        if (winner) {
            console.log("Winner: ", winner);
        }
        return winner || board.every(cell => cell !== '');
    }

    function getWinner(board) {
        const winPatterns = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];

        for (const pattern of winPatterns) {
            const [a, b, c] = pattern;
            if (board[a] && board[a] === board[b] && board[a] === board[c]) {
                return board[a];
            }
        }

        return null;
    }

    function getBestMove(board, player) {
        const availableSpots = board.reduce((acc, cell, index) => {
            if (cell === '') acc.push(index);
            return acc;
        }, []);
    
        if (getWinner(board) === player) return { score: 10 };
        if (getWinner(board) === 'X') return { score: -10 };
        if (availableSpots.length === 0) return { score: 0 };
    
        const moves = [];
    
        for (const spot of availableSpots) {
            const move = {};
            move.index = spot;
            board[spot] = player;
    
            if (player === 'O') {
                const result = getBestMove(board, 'X');
                move.score = result.score;
            } else {
                const result = getBestMove(board, 'O');
                move.score = result.score;
            }
    
            board[spot] = '';
            moves.push(move);
        }
    
        let bestMove;
        if (player === 'O') {
            let bestScore = -Infinity;
            for (const move of moves) {
                if (move.score > bestScore) {
                    bestScore = move.score;
                    bestMove = move.index;
                }
            }
        } else {
            let bestScore = Infinity;
            for (const move of moves) {
                if (move.score < bestScore) {
                    bestScore = move.score;
                    bestMove = move.index;
                }
            }
        }
    
        return bestMove;
    }
});
