class Solution {
public:

    bool isWin(vector<string>& board, char player)
    {
        for(int i = 0; i < 3; ++i)
        {
            if(board[i][0] == player && board[i][1] == player && board[i][2] == player)
                return true;
        }
        for(int i = 0; i < 3; ++i)
        {
            if(board[0][i] == player && board[1][i] == player && board[2][i] == player)
                return true;
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;
        return false;
    }

    bool validTicTacToe(vector<string>& board) {
        int n = int(board.size());
        int count_x = 0, count_o = 0;
        for(auto row:board)
        {
            for(auto c:row)
            {
                if(c == 'X')
                    ++count_x;
                else if(c == 'O')
                    ++count_o;
            }
        }
        if(count_o > count_x || count_x - count_o > 1) 
            return false;
        bool is_x_win = isWin(board, 'X');
        bool is_o_win = isWin(board, 'O');
        if(is_x_win && is_o_win) return false;
        if(is_x_win && (count_x - count_o) != 1) return false;
        if(is_o_win && (count_x != count_o)) return false;
        return true;
    }
};
