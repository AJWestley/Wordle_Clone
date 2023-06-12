import pygame as pg
import word

def check_hovered_over(x, y, width, height):
    return (pg.mouse.get_pos()[0] > x and pg.mouse.get_pos()[0] < x + width and
            pg.mouse.get_pos()[1] > y and pg.mouse.get_pos()[1] < y + height)


pg.init()
pg.font.init()

screen = pg.display.set_mode((480, 720))
pg.display.set_caption('Wordle')

puzzle = word.Word()

outline_block_coords = [[71, 142, 213, 284, 355], [100, 180, 260, 340, 420, 500]]
inner_block_coords = [[75, 146, 217, 288, 359], [104, 184, 264, 344, 424, 504]]
outer_block_dimensions = 65
inner_block_dimensions = 57
new_puzzle_button_width, new_puzzle_button_height = 200, 60
new_puzzle_button_x, new_puzzle_button_y = screen.get_width() / 2 - new_puzzle_button_width / 2, screen.get_height() - 120

running = True
clock = pg.time.Clock()

invalid_word_timer = 0

while running:
    clock.tick(60)
    if invalid_word_timer >= 0:
        invalid_word_timer -= 0.015

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_BACKSPACE:
                puzzle.backspace()
            elif event.key == pg.K_RETURN:
                if puzzle.get_valid_word():
                    puzzle.confirm_input()
                else:
                    invalid_word_timer = 1
            else:
                puzzle.input(event.unicode)
        elif event.type == pg.MOUSEBUTTONDOWN and check_hovered_over(new_puzzle_button_x, new_puzzle_button_y,
                                                                     new_puzzle_button_width, new_puzzle_button_height):
            puzzle.new_puzzle()

    #Draw begin
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill ((20, 20, 20))

    font = pg.font.Font(None, 60)
    text = font.render('W O R D L E', True, (215, 210, 220))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=20)
    background.blit(text, textpos)

    screen.blit(background, (0, 0))

    pg.draw.rect(screen, (100, 100, 100), (30, 70, background.get_width() - 60, 2))

    for i in range(puzzle.ROWS):
        for j in range(puzzle.COLUMNS):
            outline_colour = (200, 200, 200)
            if puzzle.get_inputs()[i][j] == '':
                outline_colour = (100, 100, 100)
            pg.draw.rect(screen, outline_colour, (
            outline_block_coords[0][j], outline_block_coords[1][i], outer_block_dimensions, outer_block_dimensions))
            inner_block_colour = (20, 20, 20)
            if puzzle.get_checked(i, j) == puzzle.TOTALLY_WRONG:
                inner_block_colour = (70, 70, 70)
            elif puzzle.get_checked(i, j) == puzzle.WRONG_PLACE:
                inner_block_colour = (175, 175, 30)
            elif puzzle.get_checked(i, j) == puzzle.CORRECT:
                inner_block_colour = (50, 150, 50)
            pg.draw.rect(screen, inner_block_colour, (
            inner_block_coords[0][j], inner_block_coords[1][i], inner_block_dimensions, inner_block_dimensions))
            letter_font = pg.font.Font(None, 64)
            letter = letter_font.render(puzzle.get_inputs()[i][j], True, (200, 200, 200))
            textpos = letter.get_rect(centerx=inner_block_coords[0][j] + inner_block_dimensions / 2, centery=inner_block_coords[1][i] + inner_block_dimensions / 2)
            screen.blit(letter, textpos)

    new_puzzle_button_colour = (100, 100, 100)
    if check_hovered_over(new_puzzle_button_x, new_puzzle_button_y, new_puzzle_button_width, new_puzzle_button_height):
        new_puzzle_button_colour = (200, 200, 200)

    letter_font = pg.font.Font(None, 32)
    new_puzzle_button_text = letter_font.render('New Puzzle', True, new_puzzle_button_colour)
    new_puzzle_button_text_pos = letter.get_rect(centerx=new_puzzle_button_x+new_puzzle_button_width/5,
                                                 centery=new_puzzle_button_y+5*new_puzzle_button_height/7)

    pg.draw.rect(screen, new_puzzle_button_colour, (new_puzzle_button_x, new_puzzle_button_y, new_puzzle_button_width, new_puzzle_button_height))
    pg.draw.rect(screen, (20, 20, 20), (new_puzzle_button_x + 5, new_puzzle_button_y + 5, new_puzzle_button_width - 10, new_puzzle_button_height - 10))
    screen.blit(new_puzzle_button_text, new_puzzle_button_text_pos)

    faded = pg.Surface((background.get_width(), 100))
    faded.set_alpha(180)
    faded.fill((0, 0, 0))

    if puzzle.check_correct():
        screen.blit(faded, (0, background.get_height() / 3 - faded.get_height() / 2))
        letter = letter_font.render('Good job!', True, (200, 200, 200))
        textpos = letter.get_rect(centerx=faded.get_width()/2, centery=background.get_height()/3)
        screen.blit(letter, textpos)
    elif puzzle.get_row_at() == 6:
        screen.blit(faded, (0, background.get_height() / 3 - faded.get_height() / 2))
        letter = letter_font.render(f'Unlucky! The word was {puzzle.get_answer().lower()}!', True, (200, 200, 200))
        textpos = letter.get_rect(centerx=faded.get_width() / 2, centery=background.get_height() / 3)
        screen.blit(letter, textpos)
    elif invalid_word_timer > 0:
        screen.blit(faded, (0, background.get_height() / 3 - faded.get_height() / 2))
        letter_font = pg.font.Font(None, 32)
        letter = letter_font.render('Invalid word', True, (200, 200, 200))
        textpos = letter.get_rect(centerx=faded.get_width() / 2, centery=background.get_height() / 3)
        screen.blit(letter, textpos)

    pg.display.flip()
    #Draw end
