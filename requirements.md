# Software Requirements

## Vision

1. What is the vision of this product?

    A text adventure game that changes as you play. This game is a story based text adventure, where you are a treasure hunter looking for an idol that grants youth and power. Along your journey you will traverse through 6 different environments, these environments will have a random chance of firing off a scenario. For example, in the rain forest you could get lucky and get a reward room, or you could be faced with a tiger straight from the start. This adds replay ability to the game because no one game will be the same. Items are randomized, with one given at the start, and other potentially found throughout a game. You must also manage health and stamina, as if your health runs out, its game over. If your stamina runs out, you wont be able to succeed on as many decisions, even if you have the right item for the area. At the end you will be faced with a challenge to get the idol to win the game! This will all be text based in the CLI.

2. What pain point does this project solve?

    This app will solve boredom and will provide the user with an entertaining story and replay ability.

3. Why should we care about your product?
    
    It's a unique, randomly generate text adventure experience that provides replayability

## Scope (In/Out)

1. IN - What will your product do

    This app will provide a re-playable unique experience on every new play through. Every decision the player will make
    will have different outcomes, this make it so each play through does not feel stale. This game will also give players different challenges to overcome
    via "puzzle rooms" to make the game feel more engaging.

2. OUT - What will your product not do.

    This game is purely text based so there will not be any visuals outside of text.

3. What will your MVP functionality be?
    
    Mvp is making a normal mode, where there is no greater/ lesser chance to get dangerous rooms/reward rooms.

4. What are your stretch goals?
   - Creating additional difficulties (easy and hard).
   - Adding additional languages for Non-English speakers

# Stretch

1. What stretch goals are you going to aim for?
    
    Both if we are able. Modes over language though.

Functional Requirements
List the functionality of your product. This will consist of tasks such as the following:

- Players can enter their name to add to a personalized experience
- Players can make different decisions throughout their adventure
- Resoruce management via Items/HP/Stamina
- Potential puzzles players must solve

Data Flow

Data flows in a linked list type of style. Each "Node" will be a different environment and in each will have randomly selected events. This continues until we either reach the end
or reach a "game over" by reaching 0 hit points.


Non-Functional Requirements (301 & 401 only)

Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.

- Scalability - The game will be able to have more environments, and events to go with each added environment. There can also
be new events that can be created.
- Compatability - As long as the player has a terminal they can run the game.
- Maintainability - The player won't have to run any outside imports since it will run solely off the terminal command line.