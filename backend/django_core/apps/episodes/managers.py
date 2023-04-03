from apps.user.mixins.username_with_discriminator import (
    UsernameWithDiscriminatorManager,
)

from treebeard.mp_tree import MP_NodeManager


class EpisodeCommentManager(MP_NodeManager, UsernameWithDiscriminatorManager):
    pass
