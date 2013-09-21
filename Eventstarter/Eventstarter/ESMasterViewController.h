//
//  ESMasterViewController.h
//  Eventstarter
//
//  Created by Rohit Sanbhadti on 9/21/13.
//  Copyright (c) 2013 Eventstarter. All rights reserved.
//

#import <UIKit/UIKit.h>

#import <CoreData/CoreData.h>

@interface ESMasterViewController : UITableViewController <NSFetchedResultsControllerDelegate>

@property (strong, nonatomic) NSFetchedResultsController *fetchedResultsController;
@property (strong, nonatomic) NSManagedObjectContext *managedObjectContext;

@end
