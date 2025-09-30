using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            int indexOfGuess = 0;
            foreach (var comboBox1 in mastermindBoard.Controls.OfType<ComboBox>())
            {
                comboBox1.Tag = indexOfGuess;
                comboBox1.SelectedIndexChanged += dropdownClick;

                indexOfGuess++;
                if (indexOfGuess == 3)
                {
                    indexOfGuess = 0;
                }
            }

            foreach (var submit1 in mastermindBoard.Controls.OfType<Button>())
            {
                submit1.Click += submitUserColourGuess;
            }

            int indexOfStatus = 0;

            int statusGroupIndex = 0;
            foreach (var statusBox in mastermindBoard.Controls.OfType<PictureBox>())
            {
                statusBox.Tag = statusGroupIndex;

                if (indexOfStatus == 3)
                {
                    statusGroupIndex++;
                    indexOfStatus = 0;
                } else
                {
                    indexOfStatus++;
                }
            }
        }

        string[] colours = { "Red", "Green", "Blue" , "Yellow", "Purple", "Black"};
        string[] computerGuess = new string[4];


        string[] playerGuess = new string[4];

        int playerRound = 0;

        void generateRandomColours()
        {
            Random random = new Random();

            for (int i = 0; i < 4; i++)
            {
                int colourI = random.Next(0, colours.Length);
                string colour = colours[colourI];

                computerGuess[i] = colour;
            }

            string computerGuessText = "";
            for (int i = 0; i < 4; i++)
            {
                computerGuessText += (computerGuess[i] + " ");
            }
            MessageBox.Show(computerGuessText);
        }

        bool gameStarted = false;
        string[] currentKnownColours = new string[4];

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            gameStarted = true;
            generateRandomColours();
        }

        private void dropdownClick(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;

            //MessageBox.Show((comboBox.SelectedIndex).ToString());

            comboBox.BackColor = Color.FromName(colours[comboBox.SelectedIndex]);

            int indexOfPlayerGuess = int.Parse(comboBox.Tag.ToString());
            playerGuess[indexOfPlayerGuess] = colours[comboBox.SelectedIndex];
        }

        private void submitUserColourGuess(object sender, EventArgs e)
        {
            playerRound++;
            Button button1 = (Button)sender;

            int colourIndex = 0;

            // colour and position correct? place coloured peg
            // white peg - colour correct, but incorrect position

            int numberOfColouredPegs = 0;
            int numberOfWhitePegs = 0;
            foreach (string playerColour in playerGuess)
            {
                for (int i = 0; i < 4; i++)
                {
                    if (playerColour == computerGuess[i])
                    {
                        numberOfColouredPegs++;
                    } else if (computerGuess.Contains(playerColour))
                    {
                        numberOfWhitePegs++;
                    }
                }
                colourIndex++;
            }

            PictureBox[] statusBoxesNow = {};
;            
            foreach (var statusBox in mastermindBoard.Controls.OfType<PictureBox>())
            {
                int statusGroupI = int.Parse(statusBox.Tag.ToString());
               
                if (statusGroupI == playerRound)
                {
                    MessageBox.Show("Added one status object");
                    statusBoxesNow.Append(statusBox);
                }
            }

            for (int i = 0; i < 4; i++)
            {
                if (numberOfColouredPegs > 0)
                {
                    statusBoxesNow[i].BackColor = Color.DarkBlue;
                    numberOfColouredPegs--;
                    continue;
                } else if (numberOfWhitePegs > 0)
                {
                    statusBoxesNow[i].BackColor = Color.DarkBlue;
                    numberOfWhitePegs--;
                    continue;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {

        }
    }
}
