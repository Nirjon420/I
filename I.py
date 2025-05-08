
### **App Name**: Meghumi
 
**Tagline**: *Let the clouds sing to you*
  
### **Overview**:
 
**Meghumi** is a friendly, playful, modern music streaming app inspired by Spotify. It will allow users to search, play, and save music directly from **YouTube**, with a clean and elegant UI. The app is focused on simplicity, mood-based listening, and vibrant visual design.
  
### **Core Features**:
 
 
1.  
**User Interface**:
 
 
  - Clean, minimal, and aesthetic UI.
 
  - **Color Palette**: 
 
    - Primary background: `#F1FEC6` (light pastel yellow)
 
    - Accent: `#A882DD` (lavender purple)
 

 
 
  - Font: Rounded modern sans-serif (e.g., Poppins or Quicksand)
 
  - Rounded UI elements (2xl corners)
 
  - Smooth animations on navigation and player transitions
 
  - Friendly microcopy throughout (e.g., “Hey dreamer, what do you want to hear today?”)
 

 
 
2.  
**User Flow**:
 
#### a. **Home Page**:
 
 
  - Greeting (based on time of day)
 
  - Quick access to: 
 
    - Trending Now (via YouTube trending music)
 
    - Recently Played
 
    - Your Playlists
 
    - Mood Categories: Chill, Workout, Focus, Happy, Rainy, Sad
 

 
 
  - Scrollable cards with thumbnail, title, and artist info
 

 
#### b. **Search Page**:
 
 
  - Search bar to input song/artist/genre
 
  - Uses YouTube API to fetch results
 
  - Result list with thumbnail, title, and a play button
 

 
#### c. **Player Page**:
 
 
  - Embedded YouTube player (minimized + fullscreen toggle)
 
  - Track title, artist, and video thumbnail
 
  - Controls: 
 
    - Play/Pause
 
    - Next/Previous (based on playlist/queue)
 
    - Loop/Shuffle
 
    - Volume slider
 

 
 
  - Option to add to Playlist or Like
 

 
#### d. **Playlist Page**:
 
 
  - User-created playlists (stored in local DB or Firebase)
 
  - Create new playlist
 
  - Add/remove songs
 
  - Play all option
 

 
#### e. **Mood Explorer**:
 
 
  - Predefined mood categories
 
  - Each mood opens a curated playlist (based on YouTube search + tags)
 

 
 
3.  
**Authentication (Optional)**:
 
 
  - Google sign-in or anonymous mode
 
  - Sync playlists with Firebase or local storage
 

 
 
4.  
**Backend & APIs**:
 
 
  - **YouTube API v3** to fetch and play songs/videos
 
  - Firebase or local storage for user data (playlist, preferences)
 

 
 
5.  
**Platform**:
 
 
  - Start with **Android (Flutter or React Native)**
 
  - Later extend to iOS and Web
 

 
 
6.  
**Limitations/Notes**:
 
 
  - Since YouTube content is streamed, background play may be limited (depending on implementation).
 
  - Monetization plan (ads or freemium model) can be added in future phases.
 

 
 

  
### **Sample UI Components**:
 
 
- **Navbar**: Home | Search | Playlist | Mood | Profile
 
- **Player Bar** (Bottom Sticky): Mini-player showing current track
 
- **Mood Card**: Soft pastel card with icon + mood label
 
- **Playlist Card**: Rounded square with song count
 
- **Search Result Item**: Thumbnail + title + artist + “Play” button
 

  
### **Tone & Copywriting Guide**:
 
 
- Use warm, poetic language. 
 
  - Instead of “No results found” → “Seems the clouds are quiet. Try another tune?”
 
  - Button example: “Let it play”, “Float away”, “Add to my sky”
 
