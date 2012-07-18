"""
Model definitions for storing market data messages.
"""

from django.db import models

class UUDIFMessage(models.Model):
    """
    A raw JSON UUDIF market message. This is typically only used on local
    development workstations.
    """

    key = models.CharField(max_length=255, unique=True,
        help_text="I'm assuming this is a unique hash for the message.")
    received_dtime = models.DateTimeField(auto_now_add=True,
        help_text="Time of initial receiving.")
    is_order = models.BooleanField(
        help_text="If True, this is an order. If False, this is history.")
    message = models.TextField(
        help_text="Full JSON representation of the message.")


    class Meta(object):
        verbose_name = "UUDIF Message"
        verbose_name_plural = "UUDIF Messages"

class OrderMessage(models.Model):
    """
    A parsed order message with the details broken out into the various fields.
    This represents a single line in a UUDIF rowset.
    """

    generated_at = models.DateTimeField(blank=True, null=True,
        help_text="When the market data was generated on the user's machine.")
    # TODO: This should probably be a ForeignKey to a Region model.
    region_id = models.PositiveIntegerField(
        help_text="Region ID the order originated from.")
    # TODO: This should probably be a ForeignKey to a Type model.
    type_id = models.BigIntegerField(
        help_text="The Type ID of the item in the order.")
    price = models.FloatField(
        help_text="Item price, as reported in the message.")
    volume_remaining = models.PositiveIntegerField(
        help_text="Number of remaining items for sale.")
    volume_entered = models.PositiveIntegerField(
        help_text="Number of items initially put up for sale.")
    minimum_volume = models.PositiveIntegerField(
        help_text="Minimum volume before the order finishes.")
    range = models.IntegerField(
        help_text="This field is stupid.")
    order_id = models.BigIntegerField(
        help_text="Unique order ID from EVE for this order.")
    is_bid = models.BooleanField(
        help_text="If True, this is a buy order. If False, this is a sell order.")
    issue_date = models.DateTimeField(
        help_text="When the order was issued.")
    duration = models.PositiveSmallIntegerField(
        help_text="The duration of the order, in seconds.")
    # TODO: This should probably be a ForeignKey to a Station model.
    station_id = models.PositiveIntegerField(
        help_text="The station that this order is in.")
    # TODO: This should probably be a ForeignKey to a Solar System model.
    solar_system_id = models.PositiveIntegerField(
        help_text="ID of the solar system the order is in.")
    is_suspicious = models.BooleanField(
        help_text="If this is True, we have reason to question this order's validity")
    message_key = models.CharField(max_length=255,
        help_text="The unique hash that of the market message.")
    uploader_ip_hash = models.CharField(max_length=255,
        help_text="The unique hash for the person who uploaded this message.")

    class Meta(object):
        verbose_name = "Order Message"
        verbose_name_plural = "Order Messages"