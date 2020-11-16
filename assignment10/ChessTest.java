package com.equatex.epy.chess;

public class ChessTest {

	private String[][] BOARD = {
            {"T", "S", "L","D","K", "L", "H", "T"},
            {"B", "B", "B","B","B", "B", "B", "B"},
            {".", ".", ".",".",".", ".", ".", "."},
            {".", ".", ".",".",".", ".", ".", "."},
            {".", ".", ".",".",".", ".", ".", "."},
            {".", ".", ".",".",".", ".", ".", "."},
            {"B", "B", "B","B","B", "B", "B", "B"},
            {"T", "S", "L","D","K", "L", "H", "T"}
          };
	
	public static void main(String[] args) {
		ChessTest me = new ChessTest();
		me.run();
	}
	
	private void run() {
		int[] start1 = {0,0};
		int[] end1 = {7,7};
		String path = getPath(start1,end1);
		System.out.println(path);
		int[] start2 = {7,7};
		int[] end2 = {0,0};
		path = getPath(start2,end2);
		System.out.println(path);
		int[] end3 = {1,0};
		int[] start3 = {6,0};
		path = getPath(start3,end3);
		System.out.println(path);
	}
	
	String getPath(int[] startPos, int[] endPos) {
		int[] delta = new int[2];
		delta[0] = endPos[0] - startPos[0];
		delta[1] = endPos[1] - startPos[1];
		

		//Based on detas figure out if whether X and Y go up or down or stay for each step on the board
		int xIncrement = 0;		//base case x does not change (vertial / column)
		int yIncrement = 0;		//base case y does not change (horisontal /row)
		if(delta[0] < 0)		//delta x negative, x should count down 
			xIncrement = -1;
		if(delta[0] > 0)		//delta x positive, x should count up
			xIncrement = 1;
		if(delta[1] < 0)		//delta y negative, y should count down
			yIncrement = -1;
		if(delta[1] > 0)		//delta y positive, y should count up
			yIncrement = 1;
		
		//Find number of steps (max(delta))
		int maxDelta = 0;
		if(Math.abs(delta[0]) > maxDelta)
			maxDelta = Math.abs(delta[0]);
		if(Math.abs(delta[1]) > maxDelta)
			maxDelta = Math.abs(delta[1]);
		
		int xPos = startPos[0];
		int yPos = startPos[1];
		String retval = "";
		for(int i = 0; i < maxDelta - 1; i++) {
			xPos = xPos + xIncrement;
			yPos = yPos + yIncrement;
			retval = retval + BOARD[yPos][xPos];
			
		}
		return retval;
			
	}

}
