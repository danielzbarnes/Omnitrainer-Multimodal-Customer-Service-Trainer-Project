from typing import Literal
from pydantic import BaseModel, Field


class ModerationResult(BaseModel):

    rationale: str = Field(default=False, description="Explanation of what was harmful and why")
    contains_pii: bool = Field(default=False, description="Whether the message contains any personally-identifiable information (PII)")
    is_unfriendly: bool = Field(default=False, description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(default=False, description="Whether unprofessional tone or content was detected")

    @computed_field
    @property
    def is_flagged(self) -> bool:
        """Whether the message should be flagged for review based on the moderation results"""
        return self.contains_pii or self.is_unfriendly or self.is_unprofessional

class TextModerationResult(ModerationResult):

    
    is_unfriendly: bool = Field(default=False, description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(default=False, description="Whether unprofessional tone or content was detected")


class ImageModerationResult(ModerationResult):

    is_disturbing: bool = Field(default=False, description="Whether the image is disturbing")
    is_low_quality: bool = Field(default=False, description="Whether the image is low quality")


class VideoModerationResult(ModerationResult):

    is_disturbing: bool = Field(default=False, description="Whether the video is disturbing")
    is_low_quality: bool = Field(default=False, description="Whether the video is low quality")


# TODO: Create AudioModerationResult class that inherits from ModerationResult and contains:
#   - transcription: str to contain the transcription of the audio
#   - contains_pii: bool to contain a flag for whether the audio contains any personally-identifiable
#       information (PII) such as names, addresses, phone numbers
#   - is_unfriendly: bool to contain a flag for whether unfriendly tone or content was detected
#   - is_unprofessional: bool to contain a flag for whether unprofessional tone or content was detected
class AudioModerationResult(ModerationResult):
    
    transcription: str = Field(default=False, description="Transcription of the audio")
    
    
