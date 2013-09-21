//
//  ESAppDelegate.h
//  Eventstarter
//
//  Created by Rohit Sanbhadti on 9/21/13.
//  Copyright (c) 2013 Eventstarter. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ESAppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

@property (readonly, strong, nonatomic) NSManagedObjectContext *managedObjectContext;
@property (readonly, strong, nonatomic) NSManagedObjectModel *managedObjectModel;
@property (readonly, strong, nonatomic) NSPersistentStoreCoordinator *persistentStoreCoordinator;

- (void)saveContext;
- (NSURL *)applicationDocumentsDirectory;

@end
