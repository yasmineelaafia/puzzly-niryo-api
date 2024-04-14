"""
    Puzzly - A puzzle game project
 
    (C) 2024 Yasmine EL AAFIA <elaafiayasmine@gmail.com>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Puzzly is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class SpeechException(Exception):
    """
    An exception that is raised when the google speech recongnition cannot understand the audio file
    """
    
    def __init__(self, msg: str, *args: object) -> None:
        """
        Args:
            msg (str): The constructor with a message
        """
        super().__init__(*args)
        self.msg = msg
        
    def __str__(self) -> str:
        """
        Returns:
            str: the message of the exception raised
        """
        return self.msg

class CommandException(Exception):
    """
    An exception that is raised when command said is not recognized
    """
    
    def __init__(self, msg: str, *args: object) -> None:
        """
        Args:
            msg (str): The constructor with a message
        """
        super().__init__(*args)
        self.msg = msg
        
    def __str__(self) -> str:
        """
        Returns:
            str: the message of the exception raised
        """
        return self.msg