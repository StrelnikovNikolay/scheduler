from scheduler import db
from scheduler.models import ManagedElement
"""
    Tree Structure looks like this:
     -TreeCategory1
        -TreeCategory2
          -TreeItem1
        -TreeCategory3
          -TreeItem1
     -TreeCategory4
        -TreeItem2

    So TreeCategories can have only 1-1 relations with each other
    And TreeCategories have a n - 1 relation to TreeItems
"""


class TreeCategory(ManagedElement):
    """
        Base class for ordering TreeLeaf classes
    """
    __mapper_args__ = {"polymorphic_identity" : "tree_category"}
    tree_category_id = db.Column(db.Integer, db.ForeignKey("managed_element.id"), primary_key = True)

    def __repr__(self):
        return "<TreeCategory %r>" % self.tree_category_id


# 1 To Many relationship from TreeCategories to TreeItems
tree_items_to_tree_categories = db.Table(
    "tree_items_to_tree_categories",
    db.Column("category_id", db.Integer, db.ForeignKey("tree_category.tree_category_id")),
    db.Column("item_id", db.Integer, db.ForeignKey("tree_item.tree_item_id"))
)


class TreeItem(ManagedElement):
    """
        Base class for items, to be ordered
    """
    __mapper_args__ = {"polymorphic_identity" : "tree_item"}
    tree_item_id = db.Column(db.Integer, db.ForeignKey("managed_element.id"), primary_key = True)

    def __init__(self, **kwargs):
        """
            parents - iterable of TreeCategory
        """
        if "parents" in kwargs.keys():
            self.categories.extend(kwargs["parents"])

    #binding to TreeCategory
    categories = db.relationship("TreeCategory", secondary = tree_items_to_tree_categories)

    def __repr__(self):
        return "<TreeItem %r>" % self.tree_item_id
