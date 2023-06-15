import tempfile

import asyncio
import edge_tts

VOICE = "en-IN-PrabhatNeural"

def gen(text):
    name = []

    async def _main() -> None:
        communicate = edge_tts.Communicate(text, VOICE)
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
            await communicate.save(temp_file.name)
            name.append(temp_file.name)
            
    asyncio.run(_main())
    
    return name[0]
