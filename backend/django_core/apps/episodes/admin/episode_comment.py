from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm

from ..models.episode_comment import EpisodeCommentModel

# Register your models here.


@admin.register(EpisodeCommentModel)
class EpisodeCommentAdmin(TreeNodeModelAdmin[EpisodeCommentModel]):
    autocomplete_fields = ["user"]
    list_filters = ["user"]
    search_fields = ["user__username", "text"]
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    form = TreeNodeForm
