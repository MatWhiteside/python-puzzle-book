import turtle


def draw_tree(depth: int) -> None:
    if depth == 0:
        return
    turtle.forward(20*depth)
    turtle.left(30)
    draw_tree(depth-1)
    turtle.right(60)
    draw_tree(depth-1)
    turtle.left(30)
    turtle.backward(20*depth)

draw_tree(5)
turtle.exitonclick()